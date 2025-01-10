# Schritt 1: Verwenden des offiziellen Node.js-Images
FROM node:18 AS build

# Schritt 2: Setzen des Arbeitsverzeichnisses
WORKDIR /app

# Schritt 3: Kopieren der package.json und package-lock.json
COPY package*.json ./

# Schritt 4: Installieren der Abhängigkeiten
RUN npm install

# Schritt 5: Kopieren des restlichen Projekts in das Container-Verzeichnis
COPY . .

# Schritt 6: Builden des React-Projekts
RUN npm run build

# Schritt 7: Verwenden des Nginx-Servers, um das gebaute Projekt zu hosten
FROM nginx:alpine

# Schritt 8: Kopieren der gebauten Dateien in das Nginx-Verzeichnis
COPY --from=build /app/build /usr/share/nginx/html

# Schritt 10: Starten von Nginx
CMD ["nginx", "-g", "daemon off;"]
