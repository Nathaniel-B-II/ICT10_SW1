from pyscript import document

def candidate_checker(e):
    club_members = ["ethan castaneda" , "kenzo cutamora" , "briel lagran" , "joaquin galura" , "kyle dela calzada" ]

    f_name = document.getElementById('first name').value
    l_name = document.getElementById('last name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not one the list.'
            f'Congratulations! {candidate}, you are a member of the Anti-Kenzo Club!')

    document.getElementById('result').innerHTML = messages[member_checker]


