from django.db.models import Q

from apps.core.models.user.user import User

def get_user_by_email(email):
    query = Q(email=email)
    return get_user_by_query(query)

def get_user_by_query(query: Q, use_lock: bool = False):
    if use_lock:
        return User.objects.select_for_update(skip_locked=True).filter(query)
    return User.objects.filter(query)