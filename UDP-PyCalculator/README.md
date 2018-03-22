#UDP-PyCalculator

<ul>
	<li>Server waits for data</li>
	<li>Client sends request in form (operator) (digit) (digit)</li>
	<li>Server will catch and request user to proceed</li>
	<li>Server calculates and sends response</li>
	<li>Client waits and displays received response</li>
	<li>Server loops</li>
</ul>
<p>Networking information is stored in separate file "networkInfo.py"</p>
<p>You must edit the data in your file in order for the client to function</p>

<pre>
	LHOST_IP = "" 
	RHOST_IP = ""
</pre>

<p>You must add the IP address of client in "" for LHOST_IP</p>
<p>You must add the IP address server in "" for RHOST_IP</p>

<ul>TODO:
	<li>Workout bugs in network wait time and time outs</li>
	<li>Implement server/client to be able to resume lost connections</li>
	<li>TBD</li>
</ul>
