from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls'))
]
string_var = "Web Monitor (Admin Portal)"
admin.site.site_header = f"{string_var}"
admin.site.site_title = "Admin Portal"
admin.site.index_title = f"Welcome To {string_var}"
