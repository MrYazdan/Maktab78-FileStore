from configs import INFO as information


def about_us():
    print(
        f"""Store name : {information["name"]}
Description : {information["description"]}
Version : {information["version"]}
"""
    )


def salam(name):
    print("Hello ", name)
