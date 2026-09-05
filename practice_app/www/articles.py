import frappe

def get_context(context):
    context.articles = frappe.get_all(
        "Article",
        filters={"status": "Published"},
        fields=["title", "name"]
    )

    context.title = "Latest News"
    context.no_cache = True
