from js import document

club_members = [
    "ethan castaneda",
    "kenzo cutamora",
    "briel lagran",
    "joaquin galura",
    "kyle dela calzada",
]


def candidate_checker(event):
    event.preventDefault()

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    if not first_name or not last_name:
        document.getElementById("result").innerHTML = "Please enter both names before verifying."
        document.getElementById("result").className = "result error"
        return

    candidate = f"{first_name} {last_name}".lower()
    is_member = candidate in club_members

    if is_member:
        document.getElementById("result").innerHTML = (
            f"Congratulations, {first_name} {last_name}! You are a confirmed member of the Anti-Kenzo Club."
        )
        document.getElementById("result").className = "result success"
    else:
        document.getElementById("result").innerHTML = (
            f"Sorry, {first_name} {last_name}. Your name is not on the approved resistance list."
        )
        document.getElementById("result").className = "result error"
