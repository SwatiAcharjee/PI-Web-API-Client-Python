
Contributing to any PI Web API client library for Python
============================


How to contribute
-----------------

The preferred workflow for contributing to scikit-learn is to fork the
main repository on GitHub, clone, and develop on a branch. Steps:

1. Fork the project repository by clicking on the 'Fork' button near the top right of the page. This creates
   a copy of the code under your GitHub user account. For more details on
   how to fork a repository see [this guide](https://help.github.com/articles/fork-a-repo/).

2. Clone your fork of the osimloeff repo from your GitHub account to your local disk:

   ```bash
   $ git clone git@github.com:YourLogin/PI-Web-API-Client-Python.git
   $ cd PI-Web-API-Client-Python
   ```

3. Create a ``feature`` branch to hold your development changes:

   ```bash
   $ git checkout -b my-feature
   ```

   Always use a ``feature`` branch. It's good practice to never work on the ``master`` branch!

4. Develop the feature on your feature branch. Add changed files using ``git add`` and then ``git commit`` files:

   ```bash
   $ git add modified_files
   $ git commit
   ```

   to record your changes in Git, then push the changes to your GitHub account with:

   ```bash
   $ git push -u origin my-feature
   ```

5. Follow [these instructions](https://help.github.com/articles/creating-a-pull-request-from-a-fork) or [this video](https://www.youtube.com/watch?v=YTbRzhQju4c)
to create a pull request from your fork. This will send an email to the committers.

