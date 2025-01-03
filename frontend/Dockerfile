FROM node:22

# 작업 디렉토리 설정
WORKDIR /test/frontend

# package.json과 package-lock.json 복사
COPY package.json package-lock.json ./

# 종속성 설치
RUN npm install

# Vite 실행 권한 추가
RUN chmod +x node_modules/.bin/vite && chmod +x node_modules/vite/bin/vite.js

# 소스 코드 복사
COPY . ./

# Vite 포트 노출
EXPOSE 5173

# 앱 실행
CMD ["npm", "run", "dev"]
