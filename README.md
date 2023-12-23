# FARM stack Todo app

Click on the image below to watch the demo video | Nhấp vào ảnh bên dưới để xem demo video.
[![demo](/demo.png)](https://youtu.be/3Kn24eFKV1s)

## Technologies | Công nghệ

- Backend: FastAPI, Python
- Frontend: React, TypeScript, Tailwind CSS, Vite, Yarn
- Database: MongoDB (NoSQL)
- Container: Docker.

## Installation | Cài đặt

Clone this repository | Tải về kho lưu trữ này

```shell
$ git clone https://github.com/vinhgiga/farm-stack-todo-app
```

### Localhost

#### Requirements | Yêu cầu:

- python 3.10
- NodeJS 20.10 LTS
- MongoDB Community Server application.

#### Run app | Chạy ứng dụng:

- Launch MongoDB server | Chạy MongoDB sever
- Backend: Open Terminal and run the following commands | Mở terminal và chạy lệnh dưới đây

	```shell
	$ cd farm-stack-todo-app
	$ cd backend
	```

  - On Windows | Trên Windows:

	```powershell
	$ python -m venv venv
	$ venv/Scripts/activate
	$ python -m pip install -r requirements.txt
	$ python main.py
	```

  - On macOS, Linux | Trên macOS, Linux:

    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ python3 -m pip install -r requirements.txt
    $ python3 main.py
    ```

- Frontend: Open the new Terminal and run the following commands | Mở terminal mới và chạy lệnh dưới đây:

	```shell
	$ cd farm-stack-todo-app
	$ cd frontend
	$ npm install -g yarn
	$ yarn
	$ yarn dev
	```

- Launch Google Chrome browser and type [localhost:5173](http://localhost:5173/) into the URL address bar | Mở trình duyệt Google Chrome và nhập [localhost:5173](http://localhost:5173/) vào thanh địa chỉ URL.

### Docker containers

#### Requirements | Yêu cầu

- Docker Desktop
- Docker Hub account
- 40+ GB, SSD hard disk
- 8+ GB RAM

#### Run app | Chạy ứng dụng

- Launch Docker Desktop and log in Docker Hub account | Chạy Docker Desktop và đăng nhập tài khoản Docker Hub
- Run the following commands on terminal | Chạy lệnh dưới đây trên terminal

	```shell
	$ cd farm-stack-todo-app
	$ docker-compose up
	```

- Launch Google Chrome browser and type [localhost:3000](http://localhost:3000/) into the URL address bar | Mở trình duyệt Google Chrome và nhập [localhost:3000](http://localhost:3000/) vào thanh địa chỉ URL.

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.
