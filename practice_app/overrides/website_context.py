def website_context(context):
    print("========== WEBSITE CONTEXT ==========")
    print("Website context hook called")

    context["my_key"] = "Hello from Website Context!"