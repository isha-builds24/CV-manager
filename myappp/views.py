from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import io
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
# Create your views here.
# def save_profile(request):
#     from django.shortcuts import render, redirect


# redirect to homepage
# def dashboard(request):
#     q=request.GET.get('q','').strip()
#     resumes=Profile.objects.all().order_by('-id')
#     if q:
#         resumes= resumes.filter(Q(name__icontains=q) | Q(email__icontains=q))
#     return render(request,'myappp/modern-dashboard.html',{'resumes':resumes})

# def dashboard(request):
#     q = request.GET.get('q', '').strip()
#     resumes = Profile.objects.all().order_by('-id')
    
#     if q:
#         resumes = resumes.filter(Q(name_icontains=q) | Q(email_icontains=q))
    
#     # Add these counts for your tracking
#     total_users = User.objects.count()
#     total_cvs = Profile.objects.count()

#     context = {
#         'resumes': resumes,
#         'total_users': total_users,
#         'total_cvs': total_cvs,
#     }
#     return render(request, 'myappp/modern-dashboard.html', context)
# @login_required
# def dashboard(request):
#     q = request.GET.get('q', '').strip()
#     profiles = Profile.objects.filter(owner=request.user)

#     if request.user.is_authenticated:
#         if request.user.is_superuser:
#             profiles = Profile.objects.all()
#         else:
#             profiles = Profile.objects.filter(owner=request.user)
#     else:
#         profiles = Profile.objects.none()

#     if q:
#         profiles = profiles.filter(
#             Q(name__icontains=q) | Q(email__icontains=q)
#         )

#     context = {
#         'profiles': profiles.order_by('-id'),
#         'total_users': User.objects.count(),
#         'total_cvs': Profile.objects.count(),
#     }
#     return render(request, 'myappp/modern-dashboard.html', context)

@login_required
def dashboard(request):
    q = request.GET.get('q', '').strip()
    profiles = Profile.objects.filter(owner=request.user)

    if q:
        profiles = profiles.filter(
            Q(name__icontains=q) | Q(email__icontains=q)
        )

    context = {
        'profiles': profiles.order_by('-id'),
        'total_users': User.objects.count(),
        'total_cvs': Profile.objects.count(),
    }
    return render(request, 'myappp/modern-dashboard.html', context)

@login_required
def save_profile(request):
    if request.method == "POST":
        # Step 1: Get the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        summary = request.POST.get('summary')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')

        # Step 2: Save data into database
        profile = Profile(
            owner =request.user,
            name=name, email=email, phone=phone,
            degree=degree, school=school, university=university,
            summary=summary, previous_work=previous_work, skills=skills,
        )
        profile.save()
        return redirect('dashboard')

        # Step 3: Send the user somewhere
        #return redirect('dashboard')

    # If it's not a POST (someone just opened the URL), show the form
    return render(request,'myappp/modern_create_profile.html')

@login_required
def resume(request,id):
    #user_profile=Profile.objects.get(id=id)
    user_profile = get_object_or_404(Profile, id=id , owner=request.user)
    return render(request,'myappp/modern-resume.html',{'user_profile':user_profile})

# making the CV template into pdf
@login_required
def download_resume(request,id):
    user_profile = get_object_or_404(Profile,id=id , owner=request.user)
    template_path = 'myappp/download_resume.html'
    context = {'profile':user_profile}
    template=get_template(template_path)
    html= template.render(context)

    # setting up response
    response= HttpResponse(content_type='application/pdf')
    safe_name= user_profile.name.replace('','_')
    #response['Content-Disposition']= f'attachment; filename={user_profile.name}_CV.pdf' # this will make the file name
    response['Content-Disposition']= f'attachment; filename={safe_name}_CV.pdf'
    # making conversion
    pisa_status=pisa.CreatePDF(io.BytesIO(html.encode('UTf-8')),dest=response,encoding='UTF-8')
    if pisa_status.err:
        return HttpResponse('Error generating PDF',status=500)
    return response

@login_required
def edit_profile(request, id):
  profile = get_object_or_404(Profile, id=id, owner=request.user)

  if request.method == "POST":
    profile.name = request.POST.get("name")
    profile.email = request.POST.get("email")
    profile.phone = request.POST.get("phone")
    profile.degree = request.POST.get("degree")
    profile.school = request.POST.get("school")
    profile.university = request.POST.get("university")
    profile.summary = request.POST.get("summary")
    profile.previous_work = request.POST.get("previous_work")
    profile.skills = request.POST.get("skills")
    profile.save()
    return redirect("dashboard")

  return render(
      request, "myappp/modern_create_profile.html", {"user_profile": profile}
  )

@login_required
@require_POST
def delete_profile(request, id):
  profile = get_object_or_404(Profile, id=id, owner=request.user)
  profile.delete()
  return redirect("dashboard")

def signup(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request,'myappp/signup.html',{'form' : form})


# @login_required
# def cv_list_view(request):
#     if request.user.is_superuser:
#         # You (the admin) see all profiles created on the platform
#         profiles = Profile.objects.all()
#     else:
#         # Regular users only see profiles where they are the owner
#         profiles = Profile.objects.filter(owner=request.user)
        
#     return render(request, 'myappp/modern-dashboard.html', {'profiles': profiles})









   