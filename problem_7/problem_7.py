"""
Author: Ramiz Raja
Created on: 12/01/2020

Problem: HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data
structure we learned previously. There are many different implementations of HTTP Routers such as regular expressions
or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post"
and figure out what content to return. In a dynamic web server, the content will often come from a block of code
called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the
Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would
probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling
requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the
right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with
a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split
things would be on the parts of the path that are separated by slashes ("/").
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes.
We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

A RouteTrie will store our routes and their associated handlers

Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes
 and associated handlers. It should also support adding a handler by path and looking up a handler by path.
 All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page.
Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, ...):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, ...):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

    def lookup(self, ...):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


    def split_path(self, ...):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
"""


class RouteTrieNode(object):
    def __init__(self, handler = None, is_leaf=False):
        self.children = {}
        self.handler = handler
        self.is_leaf = is_leaf

    def __iter__(self):
        for key in self.children:
            yield key

    def add(self, path: str):
        self.children[path] = RouteTrieNode()

    def __repr__(self):
        return str([c for c in self])


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler, True)

    def insert(self, paths, handler):
        # Add all the required nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if len(paths) == 0:
            return

        current_node = self.root
        for path in paths:
            if path not in current_node:
                current_node.add(path)

            current_node = current_node.children[path]

        current_node.is_leaf = True
        current_node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path in paths:
            if path not in current_node:
                return None
            current_node = current_node.children[path]

        return current_node


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie("root handler")

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)
        node = self.trie.find(path_parts)
        if node is None or not node.is_leaf:
            return "not found handler"
        else:
            return node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        parts = path.split("/")
        non_empty_parts = filter(lambda part: len(part) > 0, parts)
        return list(non_empty_parts)


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def tests():
    router = Router()
    not_found_handler = "not found handler"
    root_handler = "root handler"
    about_handler = "about handler"

    router.add_handler("/home/about", about_handler)

    assert_(expected=not_found_handler, actual=router.lookup("/home"))
    assert_(expected=not_found_handler, actual=router.lookup("/home/"))
    assert_(expected=about_handler, actual=router.lookup("/home/about"))

    home_handler = "home handler"
    router.add_handler("/home", home_handler)
    assert_(expected=home_handler, actual=router.lookup("/home"))

    # edge cases
    assert_(expected=root_handler, actual=router.lookup("/"))
    assert_(expected=home_handler, actual=router.lookup("/home/"))
    assert_(expected=about_handler, actual=router.lookup("/home/about/"))
    assert_(expected=not_found_handler, actual=router.lookup("/home/about/me"))
    assert_(expected=root_handler, actual=router.lookup("//"))
    assert_(expected=home_handler, actual=router.lookup("/home//"))
    assert_(expected=not_found_handler, actual=router.lookup("/home/home/"))

tests()
