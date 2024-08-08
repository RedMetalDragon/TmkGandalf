import requests

class ResumeService:
    def get_resume(self, resume_id: int) -> Resume:
        return Resume.objects.get(id=resume_id)