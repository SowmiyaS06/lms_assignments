def custom_resolver(route):
    print("Requested route:", route)

    if route == "job_application":
        return "job"

    return route