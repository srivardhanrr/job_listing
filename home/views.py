# views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import JobListing, Category
from django.views.decorators.clickjacking import xframe_options_exempt

# @xframe_options_exempt
# def job_listings(request):
#     # Get filter parameters
#     category_slug = request.GET.get('category')
#     location_state = request.GET.get('state')
#     location_city = request.GET.get('city')
#     job_type = request.GET.get('job_type')
#     view_type = request.GET.get('view', 'grid')  # 'grid' or 'list'
#
#     # Start with all active jobs
#     jobs = JobListing.objects.filter(is_active=True)
#
#     # Apply filters
#     if category_slug:
#         jobs = jobs.filter(category__slug=category_slug)
#     if location_state:
#         jobs = jobs.filter(location_state=location_state)
#     if location_city:
#         jobs = jobs.filter(location_city__icontains=location_city)
#     if job_type:
#         jobs = jobs.filter(job_type=job_type)
#
#     # Pagination
#     paginator = Paginator(jobs, 6)  # Show 6 jobs per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     # Get filter options
#     categories = Category.objects.filter(is_active=True)
#     states = JobListing.objects.values_list('location_state', flat=True).distinct()
#     cities = JobListing.objects.values_list('location_city', flat=True).distinct()
#
#     context = {
#         'jobs': page_obj,
#         'categories': categories,
#         'states': states,
#         'cities': cities,
#         'job_types': JobListing.JOB_TYPE_CHOICES,
#         'view_type': view_type,
#         'current_filters': {
#             'category': category_slug,
#             'state': location_state,
#             'city': location_city,
#             'job_type': job_type,
#         }
#     }
#
#     return render(request, 'jobs/listing.html', context)


# views.py
@xframe_options_exempt
def job_listings(request):
    # Get filter parameters
    category = request.GET.get('category')
    state = request.GET.get('state')
    view_type = request.GET.get('view', 'grid')

    # Get featured and non-featured jobs separately
    featured_jobs = JobListing.objects.filter(is_active=True, featured=True)
    new_jobs = JobListing.objects.filter(is_active=True)

    # Apply filters to both querysets
    if category:
        featured_jobs = featured_jobs.filter(category__slug=category)
        new_jobs = new_jobs.filter(category__slug=category)
    if state:
        featured_jobs = featured_jobs.filter(location_state=state)
        new_jobs = new_jobs.filter(location_state=state)

    # Paginate only new jobs
    paginator = Paginator(new_jobs, 6)
    page = request.GET.get('page')
    new_jobs_page = paginator.get_page(page)

    context = {
        'featured_jobs': featured_jobs,
        'new_jobs': new_jobs_page,
        'categories': Category.objects.filter(is_active=True),
        'states': JobListing.objects.values_list('location_state', flat=True).distinct(),
        'view_type': view_type,
        'current_filters': {
            'category': category,
            'state': state,
        }
    }

    return render(request, 'jobs/listing.html', context)