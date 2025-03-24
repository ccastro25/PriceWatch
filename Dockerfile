# https://dev.to/lucasleon/heroku-is-not-free-anymore-so-ill-teach-you-how-to-deploy-your-spring-boot-services-to-rendercom-with-maven-and-docker-aca
FROM eclipse-temurin:21-jdk-alpine as build
WORKDIR /workspace/app
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src
RUN chmod +x ./mvnw
RUN ./mvnw install -DskipTests
RUN mkdir -p target/dependency && (cd target/dependency; jar -xf ../*.jar)
FROM eclipse-temurin:21-jdk-alpine
VOLUME /tmp
ARG DEPENDENCY=/workspace/app/target/dependency
COPY --from=build ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=build ${DEPENDENCY}/BOOT-INF/classes /app
ENV PORT=9007
ENV SPRING_PROFILES_ACTIVE=prod
EXPOSE ${PORT}
HEALTHCHECK --interval=30s --timeout=3s --start-period=60s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:${PORT}/actuator/health || exit 1
ENTRYPOINT ["java","-cp","app:app/lib/*","com.example.Price_Watch.PriceWatchApplication"]