from django import template

register = template.Library()

@register.filter(name='job_class')
def job_class(value):
    mapping = {
        'Internship': 'bg-primary-subtle text-primary border border-primary-subtle',
        'Full-time': 'bg-success-subtle text-success border border-success-subtle',
        'Part-time': 'bg-warning-subtle text-warning-emphasis border border-warning-subtle',
        'Contract': 'bg-info-subtle text-info-emphasis border border-info-subtle',
        'Volunteer': 'bg-danger-subtle text-danger border border-danger-subtle',
    }
    return mapping.get(value, 'bg-secondary-subtle text-secondary')

@register.filter(name='job_icon')
def job_icon(value):
    mapping = {
        'Internship': 'bi-mortarboard-fill',
        'Full-time': 'bi-briefcase-fill',
        'Part-time': 'bi-clock-fill',
        'Contract': 'bi-file-text-fill',
        'Volunteer': 'bi-heart-fill',
    }
    return mapping.get(value, 'bi-tag-fill')
