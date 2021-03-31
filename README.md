# perfectionis
ASGI REST API framework.

This is a work in progress.

Have you ever built REST APIs that only respond 200 or 400? Have you ever built REST API with resources identifiers named get_id or insert_post? Then you are most likely using a non-standard and poor architecture. perfectionis will show you the way.

Most API frameworks put the emphasis on the concepts of routes and responses. An API is defined as a set of routes with associated functions providing content.

In this framework, you define resources. The responses and the routes associated with these resources are generated by the framework. That way, you get proper HTTP response codes and sound permission management.

In other words, this framework aims to exhaustively replicate the typical flow diagram of a REST API without letting you do all the work. Its parameterization also encourages you to use a sound back-end architecture.

perfectionis uses ASGI, a web server interface built for concurrency.

It is loosely inspired by cowboy : https://ninenines.eu/docs/en/cowboy/2.8/guide/rest_flowcharts/

I encourage you to use Erlang/OTP and cowboy.
