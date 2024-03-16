import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .utils import calc_file_result, calc_text_result


def home(request):
    return render(request, 'base.html')


@require_http_methods(["POST"])
def upload_file(request):
    skills_file = request.FILES['skills_file']
    filename = request.POST['filename']
    sorted_result = calc_file_result(skills_file)

    df = pd.DataFrame(sorted_result, columns=['Skill', 'Score'])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

    df.to_excel(response, index=False)
    return response


@require_http_methods(["POST"])
def text_file(request):
    skills = request.POST["text"]
    filename = request.POST['filename']

    sorted_result = calc_text_result(skills)

    df = pd.DataFrame(sorted_result, columns=['Skill', 'Score'])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

    df.to_excel(response, index=False)
    return response


@require_http_methods(["POST"])
def chart_file(request):
    freelancer_file = request.FILES['freelancer_skills']
    job_file = request.FILES['job_skills']
    filename = request.POST['filename']

    result = []

    freelancer_df = pd.read_excel(freelancer_file)
    job_df = pd.read_excel(job_file)

    freelancer_skills = freelancer_df['Skill'].to_list()
    freelancer_scores = freelancer_df['Score'].to_list()
    freelancers = dict(zip(freelancer_skills, freelancer_scores))

    job_skills = job_df['Skill'].to_list()
    job_scores = job_df['Score'].to_list()
    jobs = dict(zip(job_skills, job_scores))

    skills = set(job_skills).intersection(set(freelancer_skills))
    for skill in skills:
        result.append((skill, freelancers[skill], jobs[skill]))

    result.sort(key=lambda s: s[1] + s[2], reverse=True)

    df = pd.DataFrame(result, columns=['Skill', 'Freelancer', 'Job'])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

    df.to_excel(response, index=False)
    return response
