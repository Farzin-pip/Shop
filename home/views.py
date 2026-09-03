from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . import tasks
from .models import Product
from django.contrib import messages
from bucket import bucket


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detail.html', {'product': product})


class BucketHomeView(View):
    template_name = 'home/bucket.html'
    def get(self, request):
        object = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {'objects': object})


class DeleteBucketObjectView(View):
    def get(self, request, key):
        tasks.delete_bucket_object_task.delay(key)
        messages.success(request, 'Bucket Object Deleted Successfully', 'info')
        return redirect('home:bucket_home')


class DownloadBucketObjectView(View):
    def get(self, request, key):
        tasks.download_bucket_object_task.delay(key)
        messages.success(request, 'Bucket Object Downloaded Successfully', 'info')
        return redirect('home:bucket_home')


class UploadObjectView(View):
    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            messages.error(request, "Please select a file.")
            return redirect("home:bucket")

        path = bucket.save_temp_file(file)
        tasks.upload_object_task.delay(path, file.name)

        messages.success(request, "Upload started.")
        return redirect("home:bucket")