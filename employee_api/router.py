from rest_framework.routers import Route, DynamicDetailRoute, DefaultRouter

class EmployeeRouter(DefaultRouter):
    """
    A router for manage APIs.
    """
    routes = [
        Route(
            url=r'^{prefix}/*$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        )
        ,
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={
                'get': 'retrieve',
                'delete': 'destroy',
                'put': 'update'
            },
            name='{basename}-detail',
            initkwargs={'suffix': 'Detail'}
        )
        # ,
        # DynamicDetailRoute(
        #     url=r'^{prefix}/{lookup}/{methodnamehyphen}$',
        #     name='{basename}-{methodnamehyphen}',
        #     initkwargs={}
        # )
    ]