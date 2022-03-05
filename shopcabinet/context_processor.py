from .models import Category, Setting



def load_catigories(request):
    categories = Category.objects.filter(parent=None).all()
    children_query = Category.objects.filter(parent_id__in=[k.id for k in categories]).all()
    phone = Setting.objects.get(key='phone').value
    children = {}

    for child in children_query:
        if child.parent_id not in children:
            children[child.parent_id] = []
        children[child.parent_id].append(child)
    return {
        'categories': categories,
        'categoriy_children': children,
        'phone': phone,
    }


def load_setting(request):
    return {
        'setting_{}'.format(item.key): item.value for item in Setting.objects.all()
    }