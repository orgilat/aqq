# 1. בוחרים אימג' בסיס של פייתון
FROM python:3.11-slim

# 2. מתקינים כלים שצריך בשביל להריץ Selenium + Chrome ו־Java
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium-driver \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libgbm1 \
    xdg-utils \
    openjdk-17-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. מתקינים את allure
RUN wget -qO- https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.tgz | tar xvz -C /opt && ln -s /opt/allure-2.15.0/bin/allure /usr/local/bin/allure

# 4. הגדרת JAVA_HOME ו־PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# 5. מתקינים את הספריות פייתון מתוך קובץ requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. מעתיקים את כל קבצי הפרויקט פנימה
COPY . /app
WORKDIR /app

# 7. פקודת ברירת מחדל — להריץ את הטסט ולהפיק את פלט ה־Allure
CMD pytest --alluredir=allure-results && allure serve allure-results
