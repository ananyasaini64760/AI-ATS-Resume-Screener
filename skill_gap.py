def find_missing_skills(resume, job_desc):
    resume_words = set(resume.split())
    job_words = set(job_desc.split())

    missing = job_words - resume_words

    return list(missing)[:20]
