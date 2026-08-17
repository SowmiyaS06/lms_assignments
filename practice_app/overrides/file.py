


# def before_write(file_size):
#     print("========== BEFORE WRITE FILE ==========")
#     print("File size:", file_size)
def write_file(*args, **kwargs):
    print("========== CUSTOM WRITE FILE ==========")
    print("ARGS:", args)
    print("KWARGS:", kwargs)


# def delete_file(*args, **kwargs):
#     print("========== DELETE FILE ==========")