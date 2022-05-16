# bloomfs


What is **bloomfs**?

**bloomfs** is a package that contains a lot of components to use Bloom Filter for experiments or, maybe
in the future in production environments.

The design of package is very modular and high customizable in order to give the opportunity
to you to change the implementation of functions as you want.

The very modular design is due to *heavy use* of abstract classes that define the interface of certain
component.


### Idea

Why **bloomfs**? I have started working on bloomfs after the lectures of Bloom Filters that I attended
during my Master Degree at Univerisity of Pisa. The teacher, prof. Paolo Ferragina, has given me this idea.

Bloom Filters is widely used in IR systems, and is maybe a first algorithm that has given a very strong
boost of efficiency on crawlers.

But:

    1. Can we implement another kind filter based on Bloom Filter? (Idea of extension)
    2. Can we improve again the performance of Bloom Filter with different representation and different
    a diffrent hardware?

This is the main purpose of the repository.

Another purpose is:

    1. Explain how Bloom Filter work, and why it works (Jupyter notebook with Graphviz)
    2. Let you experiment
