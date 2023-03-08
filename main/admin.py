from django.contrib import admin
<<<<<<< Updated upstream
from django.contrib.auth.admin import UserAdmin
from .models import User, Tag, Task

<<<<<<< Updated upstream
=======
admin.site.register(User, UserAdmin)
=======
from .models import User, Tag, Task

>>>>>>> Stashed changes

class TaskManagerAdminSite(admin.AdminSite):
    pass


task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")


@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
<<<<<<< Updated upstream
    list_display = ('title', )
=======
    list_display = ("title",)
>>>>>>> Stashed changes


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
<<<<<<< Updated upstream
        'title', 'description', 'creation_date', 'mod_date',
        'deadline', 'status', 'priority', 'author', 'executor'
=======
        "title",
        "description",
        "creation_date",
        "mod_date",
        "deadline",
        "status",
        "priority",
        "author",
        "executor",
>>>>>>> Stashed changes
    )


@admin.register(User, site=task_manager_admin_site)
class UserAdmin(admin.ModelAdmin):
<<<<<<< Updated upstream
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'is_staff', 'role'
    )
=======
    list_display = ("username", "first_name", "last_name", "email", "is_staff", "role")
>>>>>>> Stashed changes
>>>>>>> Stashed changes
