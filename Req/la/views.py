from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.META["REMOTE_ADDR"]
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>IP: {path}</p>
    <p>User-agent: {user_agent}</p>
""")
def error(request):
    return HttpResponse("к сожалению произошла ошибка", status=400, reason="Incorrect data")
def user(request, name="Bobik_Live_YT", age = 4216785120964359246):
    return HttpResponse(f"<h2>Логин пользователя: {name}   Пароль: {age}</h2>")
