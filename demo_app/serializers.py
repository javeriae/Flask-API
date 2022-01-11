def user_serializer(user, include_all=False):

    return {
        "id": user.id,
        "name": user.name,
        "active": user.active,
        "country": user.country,
        "create_date": user.created_on.strftime('%Y-%m-%d %H:%M')
    }
