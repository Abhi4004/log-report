Analyze the Apache-style access log located at `/app/access.log` and generate a JSON summary report.

Write the output to the absolute path:

/app/report.json

Success criteria:

1. Create a valid JSON file at `/app/report.json`.
2. The JSON must contain the following fields:
   - `total_requests`
   - `unique_ips`
   - `top_path`
3. The values in the report must accurately summarize the contents of `/app/access.log`.
4. The output file must not be empty.