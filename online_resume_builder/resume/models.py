from django.shortcuts import render

def start(request):
    return render(request, 'start.html')

def home(request):
    return render(request, 'index.html')

def gen_resume(request):
    if request.method == 'POST':
        # Personal Details
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        userEmail = request.POST.get('userEmail', '')
        mobile = request.POST.get('mobile', '')
        linkedin = request.POST.get('linkedin', '')

        # Education Details
        degree = request.POST.get('degree', '')
        institutionName = request.POST.get('institutionName', '')
        graduationDate = request.POST.get('graduationDate', '')
        gpa = request.POST.get('gpa', '')

        # Project Details
        projects = []
        i = 1
        while True:
            projectTitle = request.POST.get(f'projectTitle{i}', None)
            if projectTitle is None:
                break
            project = {
                'title': projectTitle,
                'description': request.POST.get(f'description{i}', ''),
                'technologiesUsed': request.POST.get(f'technologiesUsed{i}', ''),
                'projectLink': request.POST.get(f'projectLink{i}', '')
            }
            projects.append(project)
            i += 1

        # Skills
        summary = request.POST.get('summary', '')
        technicalSkills = request.POST.get('technicalSkills', '')
        softSkills = request.POST.get('softSkills', '')
        languages = request.POST.get('languages', '')

        # Certifications
        certifications = []
        i = 1
        while True:
            certificateName = request.POST.get(f'certificateName{i}', None)
            if certificateName is None:
                break
            certification = {
                'name': certificateName,
                'issuedBy': request.POST.get(f'issuedBy{i}', ''),
                'year': request.POST.get(f'year{i}', '')
            }
            certifications.append(certification)
            i += 1

        # Awards
        awards = []
        i = 1
        while True:
            awardTitle = request.POST.get(f'awardTitle{i}', None)
            if awardTitle is None:
                break
            award = {
                'title': awardTitle,
                'issuedBy': request.POST.get(f'issuedByAward{i}', ''),
                'year': request.POST.get(f'yearAward{i}', '')
            }
            awards.append(award)
            i += 1

        # Hobbies
        hobbies = request.POST.get('hobbies', '')

        context = {
            'firstName': firstName,
            'lastName': lastName,
            'userEmail': userEmail,
            'mobile': mobile,
            'linkedin': linkedin,
            'degree': degree,
            'institutionName': institutionName,
            'graduationDate': graduationDate,
            'gpa': gpa,
            'projects': projects,
            'summary': summary,
            'technicalSkills': technicalSkills,
            'softSkills': softSkills,
            'languages': languages,
            'certifications': certifications,
            'awards': awards,
            'hobbies': hobbies,
        }
        return render(request, 'resume.html', context)

    return render(request, 'index.html')
