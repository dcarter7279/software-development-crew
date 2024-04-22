from textwrap import dedent
from crewai import Agent


class SoftwareDevelopmentAgents():
    def backend_developer_agent(self):
        return Agent(
            role='Senior Backend Developer',
            goal='Develop robust and scalable server-side logic',
            backstory=dedent("""\
			An experienced developer who specializes in building complex backend systems
			and integrating external systems and databases into complex server-side applications.
			"""),
            tools=[],
            allow_delegation=False,
            verbose=True
        )

    def frontend_developer_agent(self):
        return Agent(
            role='Lead Frontend Developer',
            goal='Create intuitive and responsive user interfaces',
            backstory=dedent("""\
			Skilled in modern JavaScript frameworks and passionate about crafting seamless user 
			experiences."""),
            tools=[],
            allow_delegation=False,
            verbose=True
        )

    def devOps_agent(self):
        return Agent(
            role='DevOps Engineer',
            goal='Ensure smooth deployments and maintain system infrastructure',
            backstory=dedent("""\
			Focuses on automation, monitoring, and system optimization to keep the development
			lifecycle efficient."""),
            tools=[],
            allow_delegation=True,
            verbose=True
        )

	def qa_tester_agent(self):
		return Agent(
			role='Chief Quality Assurance Engineer',
			goal='Identify and document bugs and ensure high quality releases.',
			backstory=dedent("""\
			A meticulous tester skilled in various testing methodoloigies to catch bugs
			before they reach production."""),
			tools=[],
			allow_delegation=True,
            verbose=True

        )
