from aiohttp.web import Response


async def index(request):
    return Response(
        text="""<h1>Лидеры цифровой трансформации, Якутия, 2023</h1>
        <h2>Задача №2</h2> 
        <p>"Сервис прогнозирования увольнения на основе вовлеченности сотрудника"</p> 
        <a href='/docs'>Документация KOLMAR HR API</a>
        <p>Команда "К"</p>""",
        content_type="text/html",
    )