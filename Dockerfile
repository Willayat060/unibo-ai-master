FROM node:20-alpine
WORKDIR /app
COPY . .
EXPOSE 3000
ENV PORT=3000
CMD ["node", "UniBo-Study-App/server.js"]
