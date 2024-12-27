FROM node:22
WORKDIR /postgreSQLtest/frontend
COPY package.json package-lock.json ./
RUN npm install 
COPY . ./
EXPOSE 5173
CMD ["npm", "run", "dev"]