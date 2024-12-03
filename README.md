# time-in-bio

This script allows you to display the current time in your telegram bio in real-time.

## Requirements

* installed `docker` on your PC or VPS

## Usage

1. Clone repo to your machine (or get files in any other way)
```bash
git clone https://github.com/acruxtech/bio_time_telethon.git
```
2. Create a new app on my.telegram.org and obtain the API ID and API HASH
3. Add obtained info with to the `.env` (you should to create this file using `.env.example` as template)
4. Run 
```bash
docker compose -f docker-compose.yml --env-file=.env up --build  
```
(add flag `-d` if you want to run in detached mode)
5. It's all!