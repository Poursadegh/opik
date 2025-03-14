# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.automation_rule_evaluator_page_public import (
    AutomationRuleEvaluatorPagePublic,
)
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.automation_rule_evaluator_write import AutomationRuleEvaluatorWrite
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.automation_rule_evaluator_public import AutomationRuleEvaluatorPublic
from ..types.llm_as_judge_code import LlmAsJudgeCode
from ..types.log_page import LogPage
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AutomationRuleEvaluatorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_evaluators(
        self,
        project_id: str,
        *,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPagePublic:
        """
        Find project Evaluators

        Parameters
        ----------
        project_id : str

        name : typing.Optional[str]

        page : typing.Optional[int]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPagePublic
            Evaluators resource

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.find_evaluators(
            project_id="projectId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators",
            method="GET",
            params={
                "name": name,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPagePublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPagePublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_automation_rule_evaluator(
        self,
        project_id: str,
        *,
        request: AutomationRuleEvaluatorWrite,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create automation rule evaluator

        Parameters
        ----------
        project_id : str

        request : AutomationRuleEvaluatorWrite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import AutomationRuleEvaluatorWrite_LlmAsJudge, OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.create_automation_rule_evaluator(
            project_id="projectId",
            request=AutomationRuleEvaluatorWrite_LlmAsJudge(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=AutomationRuleEvaluatorWrite,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_automation_rule_evaluator_batch(
        self,
        project_id: str,
        *,
        ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete automation rule evaluators batch

        Parameters
        ----------
        project_id : str

        ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.delete_automation_rule_evaluator_batch(
            project_id="projectId",
            ids=["ids"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/delete",
            method="POST",
            json={
                "ids": ids,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_evaluator_by_id(
        self,
        project_id: str,
        id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPublic:
        """
        Get automation rule by id

        Parameters
        ----------
        project_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPublic
            Automation Rule resource

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.get_evaluator_by_id(
            project_id="projectId",
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_automation_rule_evaluator(
        self,
        id: str,
        project_id: str,
        *,
        name: str,
        code: LlmAsJudgeCode,
        sampling_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        update Automation Rule Evaluator by id

        Parameters
        ----------
        id : str

        project_id : str

        name : str

        code : LlmAsJudgeCode

        sampling_rate : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from Opik import (
            LlmAsJudgeCode,
            LlmAsJudgeMessage,
            LlmAsJudgeModelParameters,
            LlmAsJudgeOutputSchema,
            OpikApi,
        )

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.update_automation_rule_evaluator(
            id="id",
            project_id="projectId",
            name="name",
            code=LlmAsJudgeCode(
                model=LlmAsJudgeModelParameters(
                    name="name",
                    temperature=1.1,
                ),
                messages=[
                    LlmAsJudgeMessage(
                        role="SYSTEM",
                        content="content",
                    )
                ],
                variables={"key": "value"},
                schema=[
                    LlmAsJudgeOutputSchema(
                        name="name",
                        type="BOOLEAN",
                        description="description",
                    )
                ],
            ),
            sampling_rate=1.1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
                "code": convert_and_respect_annotation_metadata(
                    object_=code, annotation=LlmAsJudgeCode, direction="write"
                ),
                "sampling_rate": sampling_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_evaluator_logs_by_id(
        self,
        project_id: str,
        id: str,
        *,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogPage:
        """
        Get automation rule evaluator logs by id

        Parameters
        ----------
        project_id : str

        id : str

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogPage
            Automation rule evaluator logs resource

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.automation_rule_evaluators.get_evaluator_logs_by_id(
            project_id="projectId",
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/{jsonable_encoder(id)}/logs",
            method="GET",
            params={
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LogPage,
                    parse_obj_as(
                        type_=LogPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAutomationRuleEvaluatorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find_evaluators(
        self,
        project_id: str,
        *,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPagePublic:
        """
        Find project Evaluators

        Parameters
        ----------
        project_id : str

        name : typing.Optional[str]

        page : typing.Optional[int]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPagePublic
            Evaluators resource

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.find_evaluators(
                project_id="projectId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators",
            method="GET",
            params={
                "name": name,
                "page": page,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPagePublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPagePublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_automation_rule_evaluator(
        self,
        project_id: str,
        *,
        request: AutomationRuleEvaluatorWrite,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create automation rule evaluator

        Parameters
        ----------
        project_id : str

        request : AutomationRuleEvaluatorWrite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi, AutomationRuleEvaluatorWrite_LlmAsJudge

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.create_automation_rule_evaluator(
                project_id="projectId",
                request=AutomationRuleEvaluatorWrite_LlmAsJudge(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=AutomationRuleEvaluatorWrite,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_automation_rule_evaluator_batch(
        self,
        project_id: str,
        *,
        ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete automation rule evaluators batch

        Parameters
        ----------
        project_id : str

        ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.delete_automation_rule_evaluator_batch(
                project_id="projectId",
                ids=["ids"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/delete",
            method="POST",
            json={
                "ids": ids,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_evaluator_by_id(
        self,
        project_id: str,
        id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AutomationRuleEvaluatorPublic:
        """
        Get automation rule by id

        Parameters
        ----------
        project_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutomationRuleEvaluatorPublic
            Automation Rule resource

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.get_evaluator_by_id(
                project_id="projectId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AutomationRuleEvaluatorPublic,
                    parse_obj_as(
                        type_=AutomationRuleEvaluatorPublic,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_automation_rule_evaluator(
        self,
        id: str,
        project_id: str,
        *,
        name: str,
        code: LlmAsJudgeCode,
        sampling_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        update Automation Rule Evaluator by id

        Parameters
        ----------
        id : str

        project_id : str

        name : str

        code : LlmAsJudgeCode

        sampling_rate : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from Opik import (
            AsyncOpikApi,
            LlmAsJudgeCode,
            LlmAsJudgeMessage,
            LlmAsJudgeModelParameters,
            LlmAsJudgeOutputSchema,
        )

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.update_automation_rule_evaluator(
                id="id",
                project_id="projectId",
                name="name",
                code=LlmAsJudgeCode(
                    model=LlmAsJudgeModelParameters(
                        name="name",
                        temperature=1.1,
                    ),
                    messages=[
                        LlmAsJudgeMessage(
                            role="SYSTEM",
                            content="content",
                        )
                    ],
                    variables={"key": "value"},
                    schema=[
                        LlmAsJudgeOutputSchema(
                            name="name",
                            type="BOOLEAN",
                            description="description",
                        )
                    ],
                ),
                sampling_rate=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
                "code": convert_and_respect_annotation_metadata(
                    object_=code, annotation=LlmAsJudgeCode, direction="write"
                ),
                "sampling_rate": sampling_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_evaluator_logs_by_id(
        self,
        project_id: str,
        id: str,
        *,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogPage:
        """
        Get automation rule evaluator logs by id

        Parameters
        ----------
        project_id : str

        id : str

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogPage
            Automation rule evaluator logs resource

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.automation_rule_evaluators.get_evaluator_logs_by_id(
                project_id="projectId",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/private/automations/projects/{jsonable_encoder(project_id)}/evaluators/{jsonable_encoder(id)}/logs",
            method="GET",
            params={
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    LogPage,
                    parse_obj_as(
                        type_=LogPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
