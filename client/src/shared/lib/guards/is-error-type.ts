import type { ErrorType } from "../types";

export function isErrorType(data: unknown): data is ErrorType {
    return typeof data === 'object' && data !== null && 'error' in data
}