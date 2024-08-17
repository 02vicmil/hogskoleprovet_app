One idea for where to run the server is to use something called AWS lightsail

- Pros
  - easy to setup
  - cheap (minimum 3.5 euro / month)
  - 20 GB storage, 1 vcpu, 500MB ram for the cheapest instance
- Cons
  - Using more than 5% CPU consumes so-called "compute points". If they run out, the server shuts down. They do however regenerate over time
  - Utilizing more than the allocated bandwidth for incomming + outgoing traffic (1 TB/month for the cheapest instance) will lead to expensive extra costs, like 100 euros for every extra TB used above that thresh-hold. So additional scripts may need to be deployed to ensure that it shuts down well before then if additional costs are to be avoided

You then want to connect this to cloudflare(free), which allows you to block specific regions, decrease number of bots and avoid ddos attacks etc. But note, it is not perfect
