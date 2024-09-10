import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend } from 'k6/metrics';

// Custom metrics
let responseTimeTrend = new Trend('response_time');

// Test options
export let options = {
    stages: [
        { duration: '1m', target: 100 }, // ramp up to 100 users over 1 minute
        { duration: '3m', target: 100 }, // stay at 100 users for 3 minutes
        { duration: '1m', target: 200 }, // ramp up to 200 users over 1 minute
        { duration: '3m', target: 200 }, // stay at 200 users for 3 minutes
        { duration: '1m', target: 0 },   // ramp down to 0 users over 1 minute
    ],
    thresholds: {
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'http_req_failed': ['rate<0.01'],   // Less than 1% of requests should fail
    },
};

// Main function that gets executed during the load test
export default function () {
    let res = http.get('https://analytics.airqo.net');

    // Check if the request was successful
    check(res, {
        'status was 200': (r) => r.status === 200,
        'response time is less than 500ms': (r) => r.timings.duration < 500,
    });

    // Record the response time
    responseTimeTrend.add(res.timings.duration);

    // Simulate a user pausing for a short time on the page
    sleep(1);
}
