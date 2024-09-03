# Dinosaurs

Python application for Dinosaurs Aficionados used to maintain and provide various information about all kinds of Dinosaurs.

As an application administrator you have the ability to:
* Add a kind of dinosaur 
  * Name
  * Eating classification [herbivores, omnivores, carnivores, unknown]
  * Typical Colour
  * Period they lived [triassic, jurassic, cretaceous, paleogene, neogene, unknown]
  * Average Size [tiny, very small, small, medium, large, very large, gigantic, unknown]
* Remove a kind(s) of dinosaur(s)
* Associate up to 2 images with each dinosaur
* Remove image(s) 

As a 3rd party developer wanting to intergrate with the application you have the ability to: 
* Find all the available kinds of dinosaurs (public)
* Search for a particular kind and get their images (public)
* Like your favourite (after registration)
* See your favourites (after registration)

The solution is using:
* Python 3.12 (managed by Poetry)
* Django 5.0 (with its testing suite)
* Database integration with PostgreSQL 14
* Docker Compose
* README

## Usage

First, prepare a `.env` file storing your app configuration and secrets (such as passwords). Store it into the root folder of this project. See a following example:

```env
APP_DEBUG_MODE="True"
DJANGO_SUPERUSER_EMAIL="abc@def.ghi"
DJANGO_SUPERUSER_PASSWORD="topsecret1"
DJANGO_SUPERUSER_USERNAME="admin"
POSTGRES_DB="dinopedia"
POSTGRES_HOST="db"
POSTGRES_PASSWORD="postgres"
POSTGRES_PORT="5432"
POSTGRES_USER="postgres"
```

Then inside the root folder of this project run `docker compose up --build`. The app will be available at `http://localhost`. A default administrator will be created (based on the provided environment variables `DJANGO_SUPERUSER_*`). For administration, log into the Django admin site at `http://localhost/admin/` where you can manage dinosaurs and create new users (for 3rd party developers).

For an easier API integration, a [Browsable API](https://www.django-rest-framework.org/topics/browsable-api/) is enabled at `http://localhost/api/`. Non-registered users can obtain details about all the available kinds of dinosaurs via GET request on the endpoint `/api/dinosaurs/` and retrieve details about a particular kind and get its images via GET request on the endpoint `/api/dinosaurs/<int>/` where `<int>` is a primary key.

After registration by an administrator, a developer can like their favourite dinosaurs via PUT request on the endpoint `/api/users/<name>/` where `<name>` is a username. To see your favourites dinosaurs, use GET request on the endpoint `/api/users/<name>/`. Note that both options require basic authentication and you can obtain and modify only data under your username.

## Submission

Just create a private repo out of this and send invites to collaborate/review on the following emails <cbekos@gwi.com> / <tvesela@gwi.com> / <kgiannousis@gwi.com> / <zmaxa@gwi.com> / <ecechal@gwi.com>
