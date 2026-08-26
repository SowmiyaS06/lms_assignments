from practice_app.practice_app.doctype.job_application.job_application import JobApplication


class CustomJobApplication(JobApplication):

    def on_update(self):
        print("🔥 CUSTOM JOB APPLICATION ON_UPDATE")
        super().on_update()