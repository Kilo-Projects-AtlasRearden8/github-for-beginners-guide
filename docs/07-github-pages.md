# Publishing a Free Static Site with GitHub Pages

**GitHub Pages** turns a repository into a website — free, with no hosting fees and no command line. This is perfect for portfolios, project sites, book hubs, and beginner guides like this one.

Your site will live at `https://your-username.github.io/your-repository-name/`.

## Step 1: Create a repository for your site

1. Create a new repository (see the Repositories chapter).
2. Name it something clear, like `my-website`.
3. Check **Add a README file**.
4. Click **Create repository**.

## Step 2: Add your website files

A website needs at least one HTML file. GitHub Pages looks for `index.html` as the home page.

1. On your repository page, click **Add file** > **Create new file**.
2. Name it `index.html`.
3. Paste this starter page:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>My Website</title>
   </head>
   <body>
       <h1>Welcome to My Website</h1>
       <p>This site is published for free with GitHub Pages.</p>
   </body>
   </html>
   ```

4. Click **Commit changes**.

## Step 3: Turn on GitHub Pages

1. In your repository, click the **Settings** tab.
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose `main` and folder `/ (root)`, then click **Save**.
5. Wait a minute or two. GitHub builds your site.

## Step 4: Visit your site

1. On the Pages settings page, you will see a link like:
   `https://your-username.github.io/my-website/`
2. Click it. Your site is live.

## Update your site

1. Edit `index.html` or add more files (CSS, images, pages) in your repository.
2. Commit the changes.
3. GitHub Pages rebuilds the site automatically, usually within a minute.

## Add more pages

Create `about.html`, `contact.html`, and so on. Link to them from `index.html`:

```html
<a href="about.html">About</a>
```

## Custom domains (optional)

If you own a domain name, you can connect it in the Pages settings. This is optional — the `github.io` address is free and works forever.

## Important reminders

- GitHub Pages is for **static sites** (HTML, CSS, JavaScript). It does not run server-side code like Python or PHP.
- Do not publish secrets, API keys, passwords, or personal data on a GitHub Pages site. Anything in a public repository is visible to everyone.
- Public repositories and GitHub Pages sites are free. Private repositories are also free, but Pages sites from private repos may have limits depending on your plan.

## What's next

You have now seen the core GitHub workflow. Use the first-repo checklist below to start your own project.

[Next: First-repo checklist](08-first-repo-checklist.md) | [Back to start](00-welcome.md)

---

Copyright (c) 2026 Asdale Dynamics, LLC.
