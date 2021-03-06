def user_serializer(user):

    return {
        'id': user.id,
        'name': user.name,
        'active': user.active,
        'country': user.country,
        'create_date': user.created_on.strftime('%Y-%m-%d %H:%M')
    }
