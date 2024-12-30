FROM node:22
WORKDIR /test/frontend
COPY package.json package-lock.json ./
RUN npm install 
COPY . ./
EXPOSE 5173
CMD ["npm", "run", "dev"]