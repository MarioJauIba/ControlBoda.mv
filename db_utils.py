import redis

r = redis.Redis(charset="utf-8", decode_responses=True)

# r.hset('family', mapping={
#     'name': 'Sample Family',
#     'desc': 'Sample desc',
#     'adults': 2,
#     'children': 0,
#     'phone': '3780000000'
# })

# print(r.hgetall('family:1'))
# print(r.hgetall('family'))
# print(r.hget('family', 'name'))

# data = {
#     'id': 'test',
#     'name': 'Sample Family',
#     'desc': 'Sample desc',
#     'adults': 2,
#     'children': 0,
#     'phone': '3780000000'
# }

# r.hset('my family', mapping=data)
# print(r.hgetall('family:2'))

def add(data):
    r.hset(data['id'], mapping=data)

def autoadd(data):
    key = str(len(r.keys()) + 1).zfill(3)
    data['id'] = key
    r.hset(key, mapping=data)

def get(key):
    return r.hgetall(key)

def get_all():
    response = []
    for key in r.keys():
        response.append(r.hgetall(key))

    return response

def delete_all():
    for key in r.keys():
        r.delete(key)

def confirm(key, data):
    try:
        r.hset(key, mapping={'confirmed_adults': data['confirmed_adults'], 'confirmed_children': data['confirmed_children'], 'confirmed': data['confirmed']})
    except KeyError:
        return ""
    
def get_totals() -> dict:
    adults_total = 0
    children_total = 0
    adults_total_confirmed = 0
    children_total_confirmed = 0
    adults_pending = 0
    children_pending = 0
    
    for key in r.keys():
        try:
            adults = int(r.hget(key, 'adults'))
            children = int(r.hget(key, 'children'))
            adults_total += adults
            children_total += children
            
            if r.hget(key, 'confirmed') not in ['true', 'false']:
                adults_pending += adults
                children_pending += children
            else:
                adults_total_confirmed += int(r.hget(key, 'confirmed_adults'))
                children_total_confirmed += int(r.hget(key, 'confirmed_children'))
            
        except TypeError as e:
            continue

    return {
            'adults_total': adults_total, 
            'children_total': children_total, 
            'adults_total_confirmed': adults_total_confirmed, 
            'children_total_confirmed': children_total_confirmed,
            'adults_pending': adults_pending,
            'children_pending': children_pending
        }

def generate_csv_report() -> str:
    import os
    from datetime import datetime
    from pathlib import Path
   
    datetime.today().strftime('%Y-%m-%d')
    all_invites = get_all()
    base_path = f"{os.getcwd()}/reports"
    file_date = datetime.today().strftime('%Y-%m-%d')
    Path(base_path).mkdir(exist_ok=True)
    file_path = f'{base_path}/report-{file_date}.csv'

    with open(file_path, 'w') as f:
        f.write(f'Familia, Descripcion, Adultos, Menores\n')

        for invite in all_invites:
            if 'confirmed' in invite and invite['confirmed'] == 'true':
                f.write(f"{invite['name']}, {invite['desc'].replace(',', '')}, {invite['confirmed_adults']}, {invite['confirmed_children']}\n")

    
    return file_path
