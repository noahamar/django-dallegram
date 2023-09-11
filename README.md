# Dall•e•gram

![enter image description here](https://i.imgur.com/rzqBTp2.png)

Dall•e•gram is a Django-based AI image generator website in the style of Instagram.

The website uses the OpenAI DALL•E API to generate images.

[Here's a demo.](https://django-dallegram-e10a0fded064.herokuapp.com/)

## Roadmap

Dall•e•gram is still a work-in-progress. Here's the roadmap:

- [x] Home page
- [x] Post creation
- [ ] Account creation
- [ ] Profile page
- [ ] Following
- [ ] Post interactions (like, save, comment)
- [ ] Stories

### Temporary default user

While account creation is in development, the `noahamar` user is temporary hard-coded as the default user.

## How to run locally

Create a `.env` file at the project root with the following keys:

    AWS_ACCESS_KEY_ID=<Your AWS Access Key ID>
    AWS_SECRET_ACCESS_KEY=<Your AWS Secret Access KEy>
    AWS_STORAGE_BUCKET_NAME=<Your AWS S3 bucket name>
    AWS_S3_REGION_NAME=<Your AWS region>
    OPENAI_API_KEY=<Your OpenAI API key>

Then, run:

    python manage.py migrate
    python manage.py runserver