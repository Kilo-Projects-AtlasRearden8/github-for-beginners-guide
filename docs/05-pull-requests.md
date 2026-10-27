# Pull Requests

A **pull request** (PR) is a proposal to change a repository. You say, "Here are changes I made — please review them and add them to the project." Pull requests are how people collaborate on GitHub without overwriting each other's work.

This chapter covers using pull requests on your own repository. You do not need the command line.

## The basic idea

1. You make changes (on your own copy or in a branch).
2. You open a pull request describing the changes.
3. Someone reviews the changes and leaves comments.
4. If everything looks good, the changes are **merged** into the main project.

## Step 1: Create a branch

A **branch** is a separate workspace for your changes. It keeps your work isolated until it is ready.

1. Open your repository on GitHub.
2. Click the branch selector (it says `main` by default) near the top left.
3. Type a new branch name, like `fix-about-typo`.
4. Click **Create branch**.

You are now working on the new branch. Any files you edit or add only affect this branch, not `main`.

## Step 2: Make your changes

Edit, add, or upload files exactly as described in the Repositories chapter. Every save creates a commit on your branch.

## Step 3: Open the pull request

1. After committing your changes, GitHub shows a yellow banner: "&lt;branch-name&gt; has recent pushes." Click **Compare & pull request**.
2. **Base branch:** Choose `main` (this is where the changes will go).
3. **Compare branch:** Choose your branch (for example, `fix-about-typo`).
4. **Title:** Summarize the change. Example: "Fix typo on About page."
5. **Description:** Explain what changed and why. You can reference an issue by typing `#` and the issue number.
6. Click **Create pull request**.

## Step 4: Review the changes

1. On the pull request page, click the **Files changed** tab.
2. You see a diff: red lines are removed, green lines are added.
3. To comment on a specific line, click the blue **+** icon next to the line and type your comment.
4. Click **Start a review** to collect your comments, then submit them.

## Step 5: Merge the pull request

When the changes look good:

1. Scroll to the bottom of the pull request page.
2. Click **Merge pull request**.
3. Choose **Create a merge commit** (the simplest option).
4. Click **Confirm merge**.

The changes from your branch are now part of `main`. You can delete the branch if you no longer need it.

## Pull requests on your own repo

Even if you are the only person working on a repository, pull requests are useful. They force you to pause and review your changes before they become part of the main project.

## What's next

Once your project is in good shape, you can publish a release.

[Next: Releases](06-releases.md) | [Back to start](00-welcome.md)

---

Copyright (c) 2026 Asdale Dynamics, LLC.
