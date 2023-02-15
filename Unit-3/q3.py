friends = []

def add_friend(name, phone_number, dob, native_city, website=None, instagram=None):
    friend = {'name': name, 'phone_number': phone_number, 'dob': dob, 'native_city': native_city, 'website': website, 'instagram': instagram}
    friends.append(friend)

def modify_friend(name, phone_number=None, dob=None, native_city=None, website=None, instagram=None):
    for friend in friends:
        if friend['name'] == name:
            if phone_number:
                friend['phone_number'] = phone_number
            if dob:
                friend['dob'] = dob
            if native_city:
                friend['native_city'] = native_city
            if website:
                friend['website'] = website
            if instagram:
                friend['instagram'] = instagram
            break

def delete_friend(name):
    for friend in friends:
        if friend['name'] == name:
            friends.remove(friend)
            break

def get_friends_by_birth_month(month):
    return [friend for friend in friends if friend['dob'].month == month]

def get_friends_by_city(city):
    return [friend for friend in friends if friend['native_city'] == city]
