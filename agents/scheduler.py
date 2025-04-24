from utils.email_sender import send_email

class SchedulerAgent:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def schedule_interview(self, to_email, candidate_name, job_role):
        subject = f"🎯 You are shortlisted for {job_role}"
        body = f"""Hi {candidate_name},

Congratulations! 🎉
You have been shortlisted for the position of {job_role}.

Our team will contact you soon to schedule the interview.

Regards,  
HackTrail Team  
"""
        send_email(self.sender_email, self.sender_password, to_email, subject, body)
