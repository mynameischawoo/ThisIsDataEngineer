start.docker.compose.for.iceberg: open.jupyter.web open.min.io.web open.spark.history.server.web
	# Run the docker-compose file for iceberg
	docker-compose -f docker-compose.yaml up -d

stop.docker.compose.for.iceberg:
	# Stop the docker-compose file for iceberg
	docker-compose -f docker-compose.yaml down

restart.docker.compose.for.iceberg:
	@docker-compose -f docker-compose.yaml down
	@docker-compose -f docker-compose.yaml up -d && \
	sleep 20 && \
	$(MAKE) open.jupyter.web && \
	$(MAKE) open.min.io.web && \
	$(MAKE) open.spark.history.server.web

open.jupyter.web:
	# Open Jupyter web interface
	open http://localhost:8888/tree/notebooks

open.min.io.web:
	# Open MinIO web interface
	open http://localhost:9001

open.spark.master.web:
	# Open Spark Master web interface
	open http://localhost:8080

open.spark.worker.web:
	# Open Spark Worker web interface
	open http://localhost:8081	

open.spark.history.server.web:
	# Open Spark History Server web interface
	open http://localhost:18080		
